function joinQuiz() {
    const username = document.getElementById('username').value;
    const quizCode = document.getElementById('quiz_code').value;
    window.location.href = `/quiz?username=${username}&code=${quizCode}`;
}

function createQuiz() {
    const title = document.getElementById('title').value;
    const username = document.getElementById('username').value;

    fetch('/create_quiz', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title: title, username: username }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle response from server
        console.log(data);
        const quizCode = data.quiz_code;
        // Redirect to the quiz page with username and quiz code parameters
        window.location.href = `/quiz?username=${username}&code=${quizCode}`;
    })
    .catch(error => console.error('Error:', error));
}