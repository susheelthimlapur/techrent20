<template>
    
    <html>
        <body>
        <h1 style="position: fixed;padding:5cm;padding-top: 5cm;margin-top: 3cm;margin-left:-145px; top:-150px;">Request a refund</h1>
        <!-- <label for="ref" style="position: fixed; top:300px; left" >Why do you need a refund? </label><br> -->
  <!-- <input type="text" style="position: fixed; top:400px;" id="ref" name="ref"><br><br> -->
  <form>
  <div class="form-group row">
    <label for="refund" class="col-sm-2 col-form-label"><h3>Why do you need a refund?</h3></label>
    <div class="col-sm-5"><br/>
      <input type="text" class="form-control" id="inputEmail3" placeholder="Brief explanation is required">
    </div>
  </div>
    <div class="col-auto my-1">
      <button type="submit" onclick="return myFunction()" class="btn btn-primary">Submit</button>
    </div>
  
</form>
</body>
</html>
</template>

<script>
function myFunction() {
    let text = "We will notify you if the refund request is approved!";
  if (confirm(text) == true) {
    text = "You pressed OK!";
  } else {
    text = "You canceled!";
  }
  document.getElementById("demo").innerHTML = text;

}
</script>
 
<style>
    
.col-form-label{
    top:100px;
    left:60px;

}
.form-control{
    top:150px;
    right:200px;
}
.btn{
    top:150px;
    left:60px;

}
</style>