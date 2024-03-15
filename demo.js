



const test = ()=>{
    fetch('http://127.0.0.1:8000/listings')
  .then(response => {
    // Check if the response is successful (status code 200-299)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    // Parse the JSON response
    return response.json();
  })
  .then(data => {
    // Handle the JSON data
    console.log('Listing data:', data);
    // Process the data here, e.g., update the UI
  })
  .catch(error => {
    // Handle any errors
    console.error('Error fetching listing data:', error);
  });
}
test()