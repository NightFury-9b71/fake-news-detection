function show(id){
    let x = document.getElementById(id).style

    if(x.width == '4vw'){
        x.width = '30vw';
        x.opacity = "0.8";
    }
    else{
        x.width = '4vw';
        x.opacity = '0';
    }

    // x.style.width = x.style.width == '30vw' ? x.style.width = '4vw' : x.style.width = '30vw';
}