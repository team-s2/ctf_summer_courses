#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

// #define DEBUG

enum TINYVM_OP
{
    TINYVM_OP_PUSH = 0,
    TINYVM_OP_POP,
    TINYVM_OP_INPUT,
    TINYVM_OP_CMP,
    TINYVM_OP_JMP,
    TINYVM_OP_JNZ,
    TINYVM_OP_JZ,
    TINYVM_OP_STOP
};

// ... more ...
//

typedef struct __attribute__((packed))
{
    uint8_t opcode;
    uint32_t value;
} TINYVM_INST;

typedef struct
{
    uint32_t pc;
    uint32_t sp;
    uint32_t *stack;
    uint8_t *rom;
} TINYVM_CORE;

TINYVM_CORE core;

void do_push(TINYVM_CORE *c, uint32_t value)
{
    c->stack[c->sp++] = value;
}

uint32_t do_pop(TINYVM_CORE *c)
{
    return c->stack[--c->sp];
}

uint32_t do_input(TINYVM_CORE *c)
{
    uint32_t temp;
    scanf("%u", &temp);
    do_push(c, temp);
}

bool do_cmp(TINYVM_CORE *c)
{
    uint32_t a = do_pop(c);
    uint32_t b = do_pop(c);
    if (a == b)
        do_push(c, 1);
    else
        do_push(c, 0);
}

void do_jmp(TINYVM_CORE *c, uint32_t offset)
{
    c->pc += offset;
}

void do_jnz(TINYVM_CORE *c, uint32_t offset)
{
    uint32_t tmp = do_pop(c);
    if (tmp)
        c->pc += offset;
}

void do_jz(TINYVM_CORE *c, uint32_t offset)
{
    uint32_t tmp = do_pop(c);
    if (!tmp)
        c->pc += offset;
}

// it can be read from file :)
// for simple sake we put is as global variable
uint8_t vmcodes[] = {
    0x02, 0x00, 0x00, 0x00, 0x00, // 00
    0x00, 0x41, 0x41, 0x41, 0x5f, // 05
    0x03, 0x00, 0x00, 0x00, 0x00, // 10
    0x06, 0x46, 0x00, 0x00, 0x00, // 15
    0x02, 0x00, 0x00, 0x00, 0x00, // 20
    0x00, 0x69, 0x73, 0x5f, 0x73, // 25
    0x03, 0x00, 0x00, 0x00, 0x00, // 30
    0x06, 0x32, 0x00, 0x00, 0x00, // 35
    0x02, 0x00, 0x00, 0x00, 0x00, // 40
    0x00, 0x6f, 0x5f, 0x67, 0x6f, // 45
    0x03, 0x00, 0x00, 0x00, 0x00, // 50
    0x06, 0x1e, 0x00, 0x00, 0x00, // 55
    0x02, 0x00, 0x00, 0x00, 0x00, // 60
    0x00, 0x6f, 0x64, 0x21, 0x21, // 65
    0x03, 0x00, 0x00, 0x00, 0x00, // 70
    0x06, 0x0a, 0x00, 0x00, 0x00, // 75
    0x00, 0x01, 0x00, 0x00, 0x00, // 80
    0x07, 0x00, 0x00, 0x00, 0x00, // 85
    0x00, 0x00, 0x00, 0x00, 0x00, // 90
    0x07, 0x00, 0x00, 0x00, 0x00, // 95
};

uint32_t vmcodeslen = 100;

void setup_core(TINYVM_CORE *c)
{
    c->pc = 0;
    c->sp = 0;
    c->stack = malloc(512);
    // we actually don't care about overflow here
    memset(c->stack, 0, 512);
    c->rom = malloc(512);
    memset(c->rom, 0, 512);

    // load code
    memcpy(c->rom, vmcodes, vmcodeslen);
}

void main_loop(TINYVM_CORE *c)
{
    while (true)
    {
        // fetch instruction
        TINYVM_INST *inst = (TINYVM_INST *)&c->rom[c->pc];

#ifdef DEBUG
        printf("[DEBUG] opcode: 0x%x, value: 0x%x\n", inst->opcode, inst->value);
#endif
        c->pc += sizeof(TINYVM_INST);

        switch (inst->opcode)
        {
        case TINYVM_OP_PUSH:
        {
            do_push(c, inst->value);
            break;
        }
        case TINYVM_OP_POP:
        {
            do_pop(c);
            break;
        }
        case TINYVM_OP_INPUT:
        {
            do_input(c);
            break;
        }
        case TINYVM_OP_CMP:
        {
            do_cmp(c);
            break;
        }
        case TINYVM_OP_JMP:
        {
            do_jmp(c, inst->value);
            break;
        }
        case TINYVM_OP_JNZ:
        {
            do_jnz(c, inst->value);
            break;
        }
        case TINYVM_OP_JZ:
        {
            do_jz(c, inst->value);
            break;
        }
        case TINYVM_OP_STOP:
        {
            // TODO: this part of code is also need to
            // be virtualized
            uint32_t decider = do_pop(c);
            if (decider)
            {
                puts("correct");
                puts("convert those hex to ascii and place in AAA{...}");
            }
            else
            {
                puts("false");
            }
            return;
        }
        default:
            printf("invalid instruction\n");
            exit(1);
        }
    }
}

void kill_core(TINYVM_CORE *c)
{
    free(c->stack);
    free(c->rom);
}

int main(int argc, char *argv[])
{
    // initialization
    setup_core(&core);

    // non-virtualization part
    main_loop(&core);

    // deinitalizaion
    kill_core(&core);
}
