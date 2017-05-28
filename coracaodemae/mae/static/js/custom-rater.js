$(document).ready(function(){
	var options = {
	    max_value: 5,
	    step_size: 0.5,
	    readonly: true,
	    initial_value: 1,
    }
	$(".rating").rate(options);
});