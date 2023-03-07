const express = require("express")
const router = express.Router();


router.get("/", (req, res) => {
    res.send("Home")
})


router.get("/estates", (req, res) => {
    res.send("Estates list")
})

module.exports = router