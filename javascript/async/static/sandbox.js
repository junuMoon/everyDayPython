// async & await

const getTodos = async() => {

	const response = await fetch('todos/stef.json');

	if(response.status != 200){
		throw new Error('cannot fetch the data');
	}

	const data = await response.json();

	return data;
	// const response = await fetch('todos/stef.json');
	// const data = await response.json();
	// const response = await fetch('todos/kim.json');
	// const data = await response.json();
};

getTodos()
	.then(console.log)
	.catch(err => console.log(err.message));

// fetch api
// asynchronous operation에서 callback 을 쓰지 않고 promise 사용

// fetch('todos/junu.json').then((response) => {
// 	console.log('resolved', response);
// 	return response.json();
// }).then(data => {
// 	console.log(data); 
// }).catch((err) => {	
// 	console.log('rejected', err);
// });

