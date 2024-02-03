//When you create a Google form, if you route to apps script from within the form, the script you create is BOUND to the form. As opposed to just opeing apps script's website, and THEN attaching it to a form.
//The .getActiveForm() method gets the form this apps script is BOUND to
var form = FormApp.getActiveForm()

function formHandler(e) {

  //This is a response. Everytime, someone submits a form, its called a 'Response'. 
  //Thus there could be multiple subsmissions, and thus multiple responses, and that's why its data type is as an Array. In this case, we're displaying the first ever submission/response
  var submittedForms = form.getResponses()
  
  //This variable to create the index we'll use when its eing passed in submittedForms. I want to always get the most recent form submission, so i'll use the .length() method - 1. I substracted 1 because indexes start from '0'
  var numberOfResponsesIndex = submittedForms.length - 1
  
  //This is ItemResponse. It represents each prompt asking for something (the questions, multiple choice, or date element) is referred to as an "Item". 
  //This will represent the different questions/prompts, and their respective responses as well. 
  //The prompts and the answers are bundled together and are thus, in an array format. So, ItemResponse simply gives us an entryway into the pairing of each Item/Question/Prompt, with their respective Responses/answers
  const itemResponses = submittedForms[numberOfResponsesIndex].getItemResponses();

  // string is empty/null so that our 'for' loop fills it up with every cycle
  let string = {};

  for (const itemResponse of itemResponses) {

    // This is the first question/first prompt. In my form its the "First Name" prompt. Title is seen as the title of an Item/Question/Prompt.
    var firstItemResponseTitle = itemResponse.getItem().getTitle()
  

    // We can now get the response/answer of the first question. You'll do this by just going straight to the ItemREsponse pairing
    var firstItemResponseAnswer = itemResponse.getResponse()
    string[firstItemResponseTitle] = firstItemResponseAnswer

  }
  
  //I had initially wanted this to have a UUID, because DynamoDB needs one field that would always be unique. 
  //Forms API comes with a UUID method to generate some random ID's. UUID stands for Universally Unique IDentifier
  var uuidValue = Utilities.getUuid()
  let uuid = 'partitionKey'
  string[uuid] = uuidValue
  console.log(string);
  

  var payload = {
    'method' : 'post',
    'contentType': 'application/json',
    //'muteHttpExceptions': true,
    // Convert the JavaScript object to a JSON string.
    'payload' : JSON.stringify(string)
  };
  UrlFetchApp.fetch('your-lambda-function-url', payload);
  
}
