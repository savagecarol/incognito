function startLoad(){
    body = document.getElementsByTagName("body")[0]
    console.log(body)
}

function showImage(){
    document.getElementById("textUpload").style.display = "none"
    document.getElementById("imageUpload").style.display = "" 
}

function showText(){
    document.getElementById("textUpload").style.display = ""
    document.getElementById("imageUpload").style.display = "none" 
}


function changeBackground(){
    document.getElementById("header").style.backgroundColor = "#2cb9c3";
    document.getElementById("header").style.boxShadow = "0 0.0625rem 0.375rem 0 rgba(0, 0, 0, 0.1)"
}

function analyzeImage(){
    document.getElementById("loader").style.display = ""
    imageLoader = document.getElementById("imageLoader")
    const reader = new FileReader()
    reader.readAsDataURL(imageLoader.files[0])
    reader.onload = function() {
        console.log(reader.result)
        document.getElementById("previewText").src = reader.result
        Tesseract.recognize(reader.result).then(function (result){ 
    
            alert(result.text)    
            document.getElementById("loader").style.display = "none"


        })
    }

    reader.onerror = function() {
        console.log(reader.error);
    };
    

}

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



  function fade(element,delay){
    
    element = document.getElementById(element)
    var op = 1
    var timer = setInterval(function () {
        if (op <= 0){
            clearInterval(timer);
        }
        element.style.opacity = op;
        op = op - 0.1;
    }, delay);
    
    
}

function unfade(element,delay) {
    element = document.getElementById(element)
    var op = 0
    var timer = setInterval(function () {
        if (op >= 1){
            clearInterval(timer);
        }
        element.style.opacity = op;
        op =op + 0.1;
    }, delay);
}


var colorArray = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
		  '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
		  '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A', 
		  '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
		  '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC', 
		  '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
		  '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680', 
		  '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
		  '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3', 
          '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'];
          



function applyColorArray(element,delay){
    element = document.getElementById(element)
    var index = 10;
    var timer = setInterval(function () {
        if(index==45){
            index=0
        }
        element.style.color = colorArray[index];
        index = index + 1
    }, delay);
}



var text = ""
    
function TextConvert(ImageData){
    Tesseract.recognize(reader.result).then(function (result){ 
    
        text = result.text

    })
}