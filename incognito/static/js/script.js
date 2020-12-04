function myFunction(x) {
    x.classList.toggle("change");
    
    var view = document.getElementById("quick-links-mobile").style
    console.log(view)

    if(view.display === "none"){
        document.getElementById("quick-links-mobile").style.display  = "inline-block";
        document.getElementById("header").style.height  = "35vh";
    }
    else{
        document.getElementById("quick-links-mobile").style.display  = "none";
        document.getElementById("header").style.height  = "20vh";
            
    }
  } 



  function fade(element){
    console.log("fade")
  }