function exportData(){
var table = document.getElementById("tablelist");
var rows = [];
for(var i=0,row;row=table.rows[i];i++){
        column1 = row.cells[0].innerText;
        column2 = row.cells[1].innerText;
        column3 = row.cells[2].innerText;
        column4 = row.cells[3].innerText;
        column5 = row.cells[4].innerText;
        column6 = row.cells[5].innerText;
        column7 = row.cells[6].innerText;
        column8 = row.cells[7].innerText;
        column9 = row.cells[8].innerText;

        rows.push([
            column1,
            column2,
            column3,
            column4,
            column5,
            column6,
            column7,
            column8,
            column9,
        ]);
    }
    csvcontent = "data:text/csv;charset=utf-8,";
    rows.forEach(function(rowArray){
        row = rowArray.join(",");
        csvcontent += row + "\r\n";
    });
    var encodedUri = encodeURI(csvcontent);
    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("export", "Bills_Laws_Report.csv");
    document.body.appendChild(link);
    link.click();
}