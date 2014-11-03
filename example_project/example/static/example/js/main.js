$(document).ready(function () {


    var client =  new ZeroClipboard($(".copy-to-clipboard"));
    client.on("copy", function (event) {
        var target = $(event.target);
        var data = target.closest(".code-container").find("pre").text();
        var clipboard = event.clipboardData;
        clipboard.setData("text/plain", data);
        target.text('Copied!');
    });
$(".show-widget-settings").click(function() {
    $(this).closest('div').find('table').show();
    $(this).hide();
    return false;
});

$("a").click(function() {
    if (this.hash.length > 1 && this.hash.slice(0,1) == '#') {
        $(this.hash).closest('.social-widget-example').find('.show-widget-settings').click();
    }


    });
    if (window.location.hash) {
        $(window.location.hash).closest('.social-widget-example').find('.show-widget-settings').click();
    }
});