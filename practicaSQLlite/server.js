const express=require("express");
const sqlite3=require("sqlite3").verbose();

const PORT=process.env.PORT||3000;
const app=express();
const db=new sqlite3.Database("imbd.db");

app.listen(PORT,()=>{
    console.log(`server is runnig on http://localhost:${PORT}`);
});