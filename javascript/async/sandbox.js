const getTodos = (resource) => {

	return new Promise((resolve, reject) => {
		const request = new XMLHttpRequest();

		request.addEventListener('readystatechange', () => {
			if(request.readyState === 4 && request.responseText.length > 0){
				const data = JSON.parse(request.responseText);
			    resolve(data);
			} else if(request.readyState === 4 && request.responseText.length === 0){
				// console.log('fail')
				reject('error getting resouce');
			}	
		});
		request.open('GET', resource)
		request.send();
	});
};

getTodos('todos/stef.json').then(data => {
	console.log('promise resolved:', data);
	return getTodos('todos/kim.json');
}).then(data => {
	console.log('promise 2 resolved:', data);
	return getTodos('todos/junu.json');
}).then(data => {
	console.log('promise 3 resolved', data);
}).catch(err => {
	console.log('promise rejected:', err);
})

// promise example

// const getSomething = () => {

// 	return new Promise((is, real) => {
// 		// fetch somethin
// 		// is('some data');
// 		real('some error');
// 	})

// };

// getSomething().then(data => {
// 	console.log(data);
// }).catch(err => {
// 	console.log(err);
// });

// getSomething().then((data) => {
// 	console.log(data);
// }, (err) => {
// 	console.log(err);
// });

// getTodos('todos/junu.json',  (err, data) => {
// 	console.log(data);
// 	getTodos('todos/kim.json', (err, data) => {
// 		console.log(data);
// 		getTodos('todos/stef.json', (err, data) => {
// 			console.log(data);
// 		});
// 	});
// });

