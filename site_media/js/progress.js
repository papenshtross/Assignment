//Progress Bar script- by Todd King (tking@igpp.ucla.edu)
//Modified by JavaScript Kit for NS6, ability to specify duration
//Visit JavaScript Kit (http://javascriptkit.com) for script

var duration=2
var _progressWidth = 50;

var _progressBar = "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
var _progressEnd = 10;
var _progressAt = 0;


// Create and display the progress dialog.
// end: The number of steps to completion
function ProgressCreate(end) {
	// Initialize state variables
	_progressEnd = end;
	_progressAt = 0;

	// Move layer to center of window to show
	if (document.all) {	// Internet Explorer
		progress.className = 'show';
		progress.style.left = (document.body.clientWidth/2) - (progress.offsetWidth/2);
		progress.style.top = document.body.scrollTop+(document.body.clientHeight/2) - (progress.offsetHeight/2);
	} else if (document.layers) {	// Netscape
		document.progress.visibility = true;
		document.progress.left = (window.innerWidth/2) - 100+"px";
		document.progress.top = pageYOffset+(window.innerHeight/2) - 40+"px";
	} else if (document.getElementById) {	// Netscape 6+
		document.getElementById("progress").className = 'show';
		document.getElementById("progress").style.left = (window.innerWidth/2)- 100+"px";
		document.getElementById("progress").style.top = pageYOffset+(window.innerHeight/2) - 40+"px";
	}

	ProgressUpdate();	// Initialize bar
}

// Hide the progress layer
function ProgressDestroy() {
	// Move off screen to hide
	if (document.all) {	// Internet Explorer
		progress.className = 'hide';
	} else if (document.layers) {	// Netscape
		document.progress.visibility = false;
	} else if (document.getElementById) {	// Netscape 6+
		document.getElementById("progress").className = 'hide';
	}
}

// Increment the progress dialog one step
function ProgressStepIt() {
	_progressAt++;
	if(_progressAt > _progressEnd) _progressAt = _progressAt % _progressEnd;
	ProgressUpdate();
}

// Update the progress dialog with the current state
function ProgressUpdate() {
	var n = (_progressWidth / _progressEnd) * _progressAt;
	if (document.all) {	// Internet Explorer
		var bar = dialog.bar;
 	} else if (document.layers) {	// Netscape
		var bar = document.layers["progress"].document.forms["dialog"].bar;
		n = n * 0.55;	// characters are larger
	} else if (document.getElementById){
                var bar=document.getElementById("bar")
        }
	var temp = _progressBar.substring(0, n);
	bar.value = temp;
}

function Start(){
    ProgressCreate(20);
	window.setTimeout("Click()", 100);
}

function Terminate(){
    ProgressDestroy();
}

function Click() {
	if(_progressAt >= _progressEnd) {
		//ProgressDestroy();
		return;
	}
	ProgressStepIt();
	window.setTimeout("Click()", (duration-1)*1000/10);
}

function CallJS(jsStr) { //v2.0
  return eval(jsStr)
}

