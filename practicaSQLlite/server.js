const express=require("express");
const sqlite3=require("sqlite3").verbose();

const PORT=process.env.PORT||3000;
const app=express();
const db=new sqlite3.Database("imdb.db");

app.use(express.static(__dirname));

app.get("/movies",(req,res)=>{
    db.all("select*from movie",(err,rows)=>{
        res.json(rows);
    });
});

app.listen(PORT,()=>{
    console.log(`server is runnig on http://localhost:${PORT}`);
});
