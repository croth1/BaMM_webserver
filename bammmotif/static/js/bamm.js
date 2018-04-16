// based on https://stackoverflow.com/a/44505315/2272172

function validate_file_size(file, max_size) {
  var current_size = file.files[0].size
  if (current_size > max_size) {
     var max_size_mb = max_size / 1024 / 1024
     alert('Input file too large - current limit: ' + max_size_mb + ' Mb');
     $(file).val(''); //for clearing with Jquery
  }
}

function toggle_visibility(elem, hide_id) {
    var hide_obj = document.getElementById(hide_id);
    var motif_format = elem.value
    if (motif_format === "MEME") {
        hide_obj.style.display = "none";
    } else {
        hide_obj.style.display = "block";
    }
}
