var submit_count = 0

const fetchResult = async(sent) => {
	const response = await fetch('http://localhost:5000/ner', {
		method: 'POST',
	  	headers: {"Content-Type": "application/json"},
	    cache: 'no-cache',
	    body: JSON.stringify({'sentence': sent})
	}).then(async(response) => {
		if(response.ok){
			console.log('data fetched');
			data = await response.json();
			return buildNerTable(data)
		return Promise.reject(response)
		}
	}).catch((error) => {
		console.error('Could not fetch data');
	});
}

const buildNerTable = (results) => {
	let table = document.querySelector('tbody');

	results.forEach(result => {
		let row = document.createElement('tr');
		row.classList.add('ent-row');

		let sent_num = document.createElement('td');
		sent_num.textContent = submit_count;

		let colName = document.createElement('td');
		colName.textContent = result.entity

		let colType = document.createElement('td');
		colType.textContent = result.label;

		row.appendChild(sent_num);
		row.appendChild(colName);
		row.appendChild(colType);

		table.appendChild(row);
	})
}

const updateResult = async(userInput) => {
	await fetchResult(userInput.value)
}

const init = async() => {
	const submitButton = document.getElementById('submit_btn');
	const userInput = document.getElementById('input_sent');

	submitButton.addEventListener('click', async (e) => {
		submit_count += 1
		await updateResult(userInput)
	});
};

init()