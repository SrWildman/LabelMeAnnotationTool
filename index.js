
$(document).ready(function () {

  //If this changes...make sure to update location of tool.html in image attribute
  imageLocation = 'AnnotationTool/Images/';

  $.ajax({
    //get all images from imageLocation
    url: imageLocation,
    success: function (data) {
      //go through the contents of each folder
      $(data).find("a:contains(/)").each(function () {
        var folder = $(this).attr("href").split('/')[0];
        //add filter button for dataset
        $('<button class="btn btn-default filter-button" data-filter="'+folder +'"></button>').html(folder).appendTo('.btns')
        $.ajax({
          //get contents of the folder
          url: imageLocation + folder +'/',
          success: (data) => {
            var regex = new RegExp("([^\s]+(\.(jpg|jpeg|png|gif|bmp))$)")
            //filter only valid image files
            $(data).find("a").filter(function(){
                return regex.test($(this).text().toLowerCase()); 
            }).each((i, val) => {
              //add image to view
              var image = $(val).attr("href");
              $('<div class="gallery_product col-lg-3 col-md-4 col-sm-4 col-xs-6 filter ' + folder +'"></div>').html('<a href="'+ 'AnnotationTool/tool.html?actions=a&mode=f&folder='+folder+'&image='+image+'" class="'+image+'"></a>').appendTo('.row')
              $('div a[class="'+image+'"]').html('<img src="'+ imageLocation + folder +'/'+ image + '" class="img-responsive">')
            });
          }
        });
        

      });
    },
    complete: function(){
      $(".filter-button").click(function () {
        var value = $(this).attr('data-filter');

        $(".filter-button").filter(function(){
          if($(this).attr('data-filter') == value){
            $(this).attr('style','background-color:lightgray')
          }
          else{
            $(this).attr('style', null)
          }
        })
    
        if (value == "all") {
          $('.filter').show('1000');
        }
        else {
          $(".filter").not('.' + value).hide('3000');
          $('.filter').filter('.' + value).show('3000');
    
        }
      });
    
      if ($(".filter-button").removeClass("active")) {
        $(this).removeClass("active");
      }
      $(this).addClass("active");
    }
  });

});
