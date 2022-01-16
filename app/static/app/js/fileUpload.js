
// Course play list file upload
// Get a reference to the file input element
const inputElement = document.querySelector('input[id="fileUpload"]');

// Create a FilePond instance
const pond = FilePond.create(inputElement);

FilePond.setOptions({
  
  server: {
    url: '/uploadFile/',
     
  }
    
});