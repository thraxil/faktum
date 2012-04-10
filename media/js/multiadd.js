(function() {
	 this.countForms = function() {
		 return $('.fact-input').length;
	 };

	 this.addFactForm = function(idx) {
		 $("#insert-point").before("<div class=\"fact-input well\" id=\"fact-input-" + idx + "\"> \
      <input type=\"text\" name=\"title-" + idx + "\" placeholder=\"title/cue\" class=\"title-input\"/> \
      <textarea name=\"details-" + idx + "\" rows=\"5\" placeholder=\"details\"></textarea> \
      <input type=\"text\" name=\"tags-" + idx + "\" placeholder=\"tags\" /> \
</div>");
     $("#fact-input-" + idx + " .title-input").bind('focus', function(evt) {
		 if(evt.target.value === "") {
       window.addFactForm(window.countForms() + 1);
		 }
		});
	 };

	 $(".title-input").bind('focus', function(evt) {
		 if(evt.target.value === "") {
			 window.addFactForm(window.countForms() + 1);
		 }
		});
 }());
