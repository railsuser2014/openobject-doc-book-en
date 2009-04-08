
$(document).ready(function(){
  var a = $('div[path].js-kit-comments').css(
  {
    'border': '1px solid black',
    'background-color': '#e6e6e6',
    'position': 'relative',
    'float': 'right',
    'padding': '2px',
    'top': '-40px',
    'right': '-10px',
    'width': '25%',
  }).find('a').css(
  {
    'color': '#444',
    'font-size': '10pt',
  }).length;

alert(a);
  
//  $('.js-poweredBy').find('a').css(
//  {
//    'font-size': '7pt',
//  })
//  
//  $('div[permalink].js-kit-comments').css(
//  {
//    'border': '1px solid black',
//    'background-color': '#e6e6e6',
//    'padding': '2px',
//  }).find('a').css(
//  {
//    'color': '#444',
//    'font-size': '10pt',
//  })
//  
});

