// function log(message) {
// 	console.log(`${message} by me`);
// }

// log('Hello World!');
// log(1235)

// function changeName(obj) {
// 	obj.name = 'coder';
// } 

// const ellie = {name: 'ellie'};
// changeName(ellie);

// console.log(ellie);
// printAll('dream', 'comes', 'true')

// function printAll(...args) { // function declaration can be called earlier than it is defiend
// 	console.log(args.length) // hoisted
// 	for (let i = 0; i < args.length; i++) {
// 		console.log(args[i]);
// 	}
// };


// const print = function (...args) { // function expression is created when
// 	for (let i = 0; i < args.length; i++) { // the execution reaches it
// 		console.log(args[i]);
// 	}
// };

// // print('junu', 'is', 'awesome') 

// const print_arrowed = (...args) => {
// 	args = ['arrow', 'blow']
// 	for (arg of args) {
// 		console.log(arg);
// 	};
// };


const getTodos = function (callbacking) {
	callbacking('hell', 'fire');
	// console.log(`type of callbacking: ${typeof(callbacking)}`);
	console.log(callbacking);
}

getTodos((err, data) => {
	console.log(err);
	console.log(data)
});
