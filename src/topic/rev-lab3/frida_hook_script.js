console.log('Frida script has been loaded successfully.');

const MAZE_SIZE = 9 * 9;
const GRID_SIZE = 4;

var malloc_cnt = 0;
var puts_cnt = 0;
var map_address;

Interceptor.attach(Module.findExportByName(null, 'malloc'), {
    // When entering malloc, print its argument as an integer to the console.
    onEnter: function (args) {
        // console.log("malloc(" + args[0].toInt32() + ")");
    },

    // When returning from malloc, print the return value (pointer) as a hexadecimal string.
    onLeave: function (retval) {
		if (malloc_cnt == 0) {
            map_address = '0x' + retval.toString(16);
			console.log("\nMap address -> " + map_address);
		}
		malloc_cnt += 1;
    }
});

Interceptor.attach(Module.findExportByName(null, 'puts'), {
    // When entering malloc, print its argument as an integer to the console.
    onEnter: function (args) {
        if (puts_cnt == 0) {
            // console.log(ptr(map_address).toString(16));
            send(map_address, ptr(map_address).readByteArray(MAZE_SIZE * GRID_SIZE));
        }
        puts_cnt += 1;
    }
});