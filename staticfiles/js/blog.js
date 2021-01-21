$(document).ready(function() {
	/* ======= Highlight.js Plugin ======= */
    /* Ref: https://highlightjs.org/usage/ */     
    $('pre code').each(function(i, block) {
	    hljs.highlightBlock(block);
	 });

	 $(document).one('click', '.like-review', function(e) {
		$(this).html('<i class="fa fa-heart" aria-hidden="true"></i> You liked this');
		$(this).children('.fa-heart').addClass('animate-like');
		$.ajax({
      type: "POST",
      url: "/add_likes/",
      data: {
        'post-id': $(this).data("id") // from form
      },
      success: function () {
        $('#message').html("<h2>Contact Form Submitted!</h2>")
      }
    });
	});



});