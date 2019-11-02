function readURL(input) {
  if (input.files && input.files[0]) {

    var reader = new FileReader();

    reader.onload = function(e) {
      $('.image-upload-wrap').hide();

      $('.file-upload-image').attr('src', e.target.result);
      $('.file-upload-content').show();

      $('.image-title').html(input.files[0].name);
    };

    reader.readAsDataURL(input.files[0]);

  } else {
    removeUpload();
  }
}

function removeUpload() {
  $('.file-upload-input').replaceWith($('.file-upload-input').clone());
  $('.file-upload-content').hide();
  $('.image-upload-wrap').show();
}
$('.image-upload-wrap').bind('dragover', function () {
        $('.image-upload-wrap').addClass('image-dropping');
    });
    $('.image-upload-wrap').bind('dragleave', function () {
        $('.image-upload-wrap').removeClass('image-dropping');
});


// POST method implementation:

// try {
//   const data = await postData('http://example.com/answer', { answer: 42 });
//   console.log(JSON.stringify(data)); // JSON-string from `response.json()` call
// } catch (error) {
//   console.error(error);
// }

// async function postData(url = '', data = {}) {
//   // Default options are marked with *
//   const response = await fetch(url, {
//     method: 'POST', // *GET, POST, PUT, DELETE, etc.
    
//     body: JSON.stringify(data) // body data type must match "Content-Type" header
//   });
//   return await response.json(); // parses JSON response into native JavaScript objects
// }


// handle events
// [document.querySelector('#firstname'), document.querySelector('#lastname')].forEach(item => {
//   item.addEventListener('input', event => {
//       // const log = document.getElementById('#showFullName');
//       // log.textContent = event.target.value;
//       console.log(event.target.value);
//   })
// })


let showResults = function(theTarget, theResult) {
    const log = document.getElementById(theTarget);
    log.textContent = theResult;
}

let interpretResult = function(result) {
    switch (result) {
      case '0':
        return 'No Diabetic Retinopathy';
        break;
      case '1':
        return 'Mild Non-Proliferative DR';
        break;
      case '2':
        return 'Moderate Non-Proliferative DR';
        break;
      case '3':
        return 'Severe Non-Proliferative DR';
        break;
      case '4':
        return 'Proliferative DR';
        break;
      default:
        return '-';
    }
}


document.forms['uploadRetinaForm'].addEventListener('submit', (event) => {
    let form = new FormData(event.target)
    event.preventDefault();
    // TODO do something here to show user that form is being submitted
    fetch(event.target.action, {
        method: 'POST',
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        // headers: {
        //   'Content-Type': 'multipart/form-data'
        // },
        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // no-referrer, *client
        body: form // event.target is the form
    }).then((response) => {
        console.log(response);
        return response.json(); // or response.text() or whatever the server sends
    }).then((body) => {
        // TODO handle body
        console.log(body);
        showResults('showFullName', `${body["firstname"]} ${body["lastname"]}`)
        showResults('showImageName', body["imagename"])
        showResults('showDescription', body["description"])
        showResults('showResult', interpretResult(body["result"]))
    }).catch((error) => {
        // TODO handle error
        console.log(error, form);
    });
    removeUpload();
    document.getElementById("uploadRetinaForm").reset();
});

// document.getElementById("uploadRetinaForm").reset()

