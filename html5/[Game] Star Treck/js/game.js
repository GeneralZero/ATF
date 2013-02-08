var g_canvas = $("#canvas")[0];
var g_context = g_canvas.getContext("2d");
var g_canvas_width = $("#canvas").width();
var g_canvas_height = $("#canvas").height();

var g_cell_size = [25, 25]; // Width, height)
var g_table_size = [500, 500];

function draw_map_grid(){
    g_context.lineWidth = 2;
    g_context.strokeStyle = "black";
    g_context.beginPath();
    for (var i = 0; i < g_cell_size[0]; i++) {
        //Horozontal Lines
        g_context.moveTo((i*g_cell_size)/g_table_size[0],0);
        g_context.lineTo((i*g_cell_size)/g_table_size[0], g_table_size[1]);
        //Vertical Lines
        g_context.moveTo(0, (i*g_cell_size)/g_table_size[1]);
        g_context.lineTo((g_table_size[0], i*g_cell_size)/g_table_size[0]);
    };
    g_context.stroke();
}​