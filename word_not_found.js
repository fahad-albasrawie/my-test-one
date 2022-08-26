alert("Waan ku xiranahay");

const form = document.getElementById('form');
const wordField = document.getElementById('word_field');

form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});

const validateInputs = () => {
    const wordFieldValue = username.value.trim();

    if(wordFieldValue === '') {
        setError(username, 'Username is required');
    } else {
        setSuccess(username);
    }

};