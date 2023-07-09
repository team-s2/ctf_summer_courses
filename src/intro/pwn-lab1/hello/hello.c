#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define ADMIN_NAME "admin"
#define USER_NAME "user"

#define BUFFER_SIZE (32)

int get_password(char *name, char *buf)
{
	unsigned int length;
	printf("Hello %s, please tell me the length of your password\n", name);
	scanf("%d", &length);

	if (length > BUFFER_SIZE)
	{
		printf("you password is way too long");
		return -1;
	}
	else
	{
		printf("cool, input your password\n");
		return read(STDIN_FILENO, buf, BUFFER_SIZE);
	}
}

#define VERIFY "\x27\x85\x56\x4a\xb2\x29\xe7\xf1\xa6\xc0\xab\xd7\xd6\x82\xb8\x1b\x4c\x43\xb0\x33\x0d\xb2\xbe\xb8\x10\x7a\x73\x30\x0a\xf3\xff\x59"
#define KEY "\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa"

void tea_decrypt_block(uint32_t *v, uint32_t *k)
{
	uint32_t v0 = v[0], v1 = v[1], sum = 0xC6EF3720, i;	 /* set up */
	uint32_t delta = 0x9e3779b9;						 /* a key schedule constant */
	uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3]; /* cache key */
	for (i = 0; i < 32; i++)
	{ /* basic cycle start */
		v1 -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3);
		v0 -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1);
		sum -= delta;
	} /* end cycle */
	v[0] = v0;
	v[1] = v1;
}

void tea_decrypt(char *ciphertext, int len, char *key)
{
	if (len % 8 != 0)
		exit(1);

	for (int i = 0; i < len; i += 8)
	{
		tea_decrypt_block(ciphertext + i, key);
	}
}

void get_user_password(char *buf)
{
	memcpy(buf, VERIFY, BUFFER_SIZE);
	tea_decrypt(buf, BUFFER_SIZE, KEY);
}

void get_admin_password(char *buf)
{
	int fd = open("password.txt", O_RDONLY);
	if (fd < 0)
	{
		printf("something wrong\n");
		exit(-1);
	}
	read(fd, buf, BUFFER_SIZE);
	close(fd);
}

void prepare()
{
	setvbuf(stdin, 0LL, 2, 0LL);
	setvbuf(stdout, 0LL, 2, 0LL);
	alarm(60);
}

int main(int argc, char *argv[])
{
	char username[BUFFER_SIZE];
	char password[BUFFER_SIZE];
	char password_verify[BUFFER_SIZE];

	prepare(); // quite necessary

	memset(username, 0, BUFFER_SIZE * 3);

	printf("Hello there, please input your username\n");
	read(STDIN_FILENO /* 0 */, username, BUFFER_SIZE);

	if (username[strlen(username) - 1] == '\n')
		username[strlen(username) - 1] = 0;

	get_password(username, password);

	if (!strncmp(username, ADMIN_NAME, strlen(ADMIN_NAME)))
	{
		get_admin_password(password_verify);
		if (!memcmp(password, password_verify, BUFFER_SIZE))
		{
			printf("password correct! launch your shell\n");
			system("/bin/sh");
		}
		else
			goto wrong_password;
	}
	else if (!strncmp(username, USER_NAME, strlen(USER_NAME)))
	{
		get_user_password(password_verify);
		if (!memcmp(password, password_verify, BUFFER_SIZE))
		{
			printf("password correct! show your the first part of flag\n");
			printf("flag1: %s", getenv("FLAG1"));
		}
		else
			goto wrong_password;
	}
	else
		goto wrong_password;

	return 0;

wrong_password:
	printf("What's wrong with you? Are you a hacker?\n");
	printf("----------------- LOG -----------------\n");
	printf("you input name as %s (len %d)\n", username, strlen(username));
	printf("you input password as %s (len %d)\n", password, strlen(password));
	printf("---------------------------------------\n");
	return -1;
}
