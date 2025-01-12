date = new Date()
const day = date.getDate(); 
const month = date.toLocaleString('default', { month: 'long' }); 
const year = date.getFullYear();

const todayDate = ` ${day} ${month} ${year}`; 

const dateli =document.getElementById('date-text');
dateli.innerText = todayDate


const phonenumber = document.getElementById('phonenumber')

const error= document.getElementById('error');
error.style.opacity = 0;



const form = document.getElementById('submitForm');

let dataFromServer;
form.addEventListener('submit', function(event) {
    event.preventDefault();
    const phoneNumber = document.getElementById('phonenumber').value.trim();
    const error = document.getElementById('error');

    if (phoneNumber === '') {
        error.style.opacity = 1; 
        return;
    } else {
        error.style.opacity = 0;
        
        async function fetchData() {
            try {
                const response = await fetch('http://127.0.0.1:5000/api/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ phoneNumber }) 
                });
                
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                
          
                const dataFromServer = await response.json();
                console.log(dataFromServer);
                
                const ulElement = document.querySelector('.response-section-ul');
                

                dataFromServer.slice(0, 20).forEach(item => {
                    const liElement = document.createElement('li');
                    liElement.style.fontSize = '1rem';
                    liElement.textContent = `api request nr. : ${item.api_call} -  ${item.id}:  testované číslo :${item.number} data: ${item.title}`;
                    ulElement.appendChild(liElement);
                });
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }
        
        fetchData();
    }
});

          


