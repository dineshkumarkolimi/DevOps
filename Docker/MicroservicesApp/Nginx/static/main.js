document.getElementById('userForm').onsubmit = function(event) {
    event.preventDefault();
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    fetch('/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: name, email: email})
    }).then(response => response.json())
      .then(data => alert('User added: ' + JSON.stringify(data)));
};

document.getElementById('mongoForm').onsubmit = function(event) {
    event.preventDefault();
    var data = document.getElementById('mongoData').value;
    fetch('/mongo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({data: data})
    }).then(response => response.json())
      .then(data => alert('Data added: ' + JSON.stringify(data)));
};

function fetchUsers() {
    fetch('/users')
    .then(response => response.json())
    .then(data => {
        var usersDiv = document.getElementById('users');
        usersDiv.innerHTML = JSON.stringify(data.users);
    });
}

// function fetchUsers() {
//     fetch('/')
//     .then(response => response.json())
//     .then(data => {
//         var usersDiv = document.getElementById('index');
//         usersDiv.innerHTML = JSON.stringify(data.users);
//     });
// }

function fetchMongo() {
    fetch('/mongo')
    .then(response => response.json())
    .then(data => {
        var mongoDiv = document.getElementById('mongoDataList');
        mongoDiv.innerHTML = JSON.stringify(data.documents);
    });
}
