getgenv().webhook = "https://discord.com/api/webhooks/1188501479682752615/LCWS4QTpNAG508JKA2osKRtWnYNbem4T43iHJfu4LrCsnyyZrPLvyKq-c5QAJyXeWw7v"
getgenv().webhookFail = "https://discord.com/api/webhooks/1166673773588647996/adIpnyKJ0sXJ6ZIpzAxJv1KDZJS6ICCrTrcrXj4-RITeIvSUTDNxzZohjJIPjzmS3YD0" 
getgenv().userid = "870106984236609656" -- pings your discord id if it snipes a huge or titanic 
getgenv().alts = {"Dexalts_mbhrx","Dexalts_9in9e", “Dexalts_a61ng”, “Dexalts_fss4n”, “Dexalts_jhhif”} -- put usernames to hop if more than two of them are in the same server
getgenv().normalwebhook = ""
getgenv().snipeNormalPets = false -- snipes other items that are priced at 1
repeat wait() until game:IsLoaded()
if game.PlaceId == 15502339080 then
    loadstring(game:HttpGet("https://raw.githubusercontent.com/Root1527/personal/main/modified.lua"))()
else
    loadstring(game:HttpGet("https://raw.githubusercontent.com/Root1527/personal/main/silly.lua"))()
end
