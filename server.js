const express = require("express");
const app = express()


app.set("view engine", "ejs")


app.get('/', (req, res) => {
    console.log("here")
    res.render("index")
    
})

const estateRouter = require("./routes/estates")

app.use("/estates", estateRouter)

app.listen(3000)