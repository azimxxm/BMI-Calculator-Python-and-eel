result_text = document.getElementById("result");
// result_text.innerHTML = "Hello"
height = getElementById("height");
weight = getElementById("weight");

function calculate(){
    eel.bmi_calculator(height.value, weight.value)(result);
}

function result(result) {
    result_text.innerHTML = result;
}