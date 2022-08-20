console.log("im live");

function test(){
 
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://ya.ru');
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.send();
    xhr.addEventListener('readystatechange', function(){
       if(xhr.readyState == 4 && xhr.status == 200){
           let data = JSON.parse(xhr.response);
           console.log(data);
         //  alert(data.title);
           //alert(data.id);
       }
       else{
        console.log(xhr.status);
       }
    });
};
$.post("http://ya.ru","",function(data){
    console.log(data);
});