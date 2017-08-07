var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true; 
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false; 
  });
}

window.onload = init;

function checkPassword() { 
var isSecure = true;
var matchingWord = "";
var userword = document.getElementById("pw").value.toLowerCase();
var results = document.getElementById("results");
var matchingWord = "";
for (var i = 0; i < wordsList.length; i++){
    if (userword === wordsList[i]) {
        isSecure = false;
        matchingWord = wordsList[i];
        break;
}
}
if (isSecure){
    results.style.color = "green";
    results.innerHTML = "You have a secure password.";
} else {
    results.style.color = "red";
    results.innerHTML = "You do not have a secure password.";
    }

}
