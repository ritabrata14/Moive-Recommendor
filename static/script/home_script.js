//alert("Working!!!")

function checkSelection()
{
   var dropdown = document.getElementById("movie-dropdown");
   var selectedOption = dropdown.options[dropdown.selectedIndex].value;
   if (selectedOption === "")
   {
     alert("Please select a movie before recommending.");
     return false;
   }
   return true;
}