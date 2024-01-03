getgenv().failedwebhook = "https://discord.com/api/webhooks/1166673773588647996/adIpnyKJ0sXJ6ZIpzAxJv1KDZJS6ICCrTrcrXj4-RITeIvSUTDNxzZohjJIPjzmS3YD0"
local ostimeold = os.time()
repeat wait() until game:IsLoaded()
setfpscap(8)
game:GetService("RunService"):Set3dRenderingEnabled(false)
local TeleportService = game:GetService("TeleportService")
local Booths_Broadcast = game:GetService("ReplicatedStorage").Network:WaitForChild("Booths_Broadcast")
local message1 = {}
local Players = game:GetService('Players')
local PlayerInServer = #Players:GetPlayers()
local Librarys = require(game.ReplicatedStorage:WaitForChild('Library'))


for i,v in ipairs(game.Players:GetPlayers()) do
    if v.UserId ~= game.Players.LocalPlayer.UserId and v.Character then
        v.Character:ClearAllChildren()
    end
end

game.Players.PlayerRemoving: connect (function (plr)
    if plr == game.Players.LocalPlayer then
      game:GetService('TeleportService'):Teleport(game.PlaceId)
    end
end)

local bb = game:GetService("VirtualUser")
game:GetService("Players").LocalPlayer.Idled:Connect(function()
    bb:CaptureController()
    bb:ClickButton2(Vector2.new())
end)


local function processListingInfo(uid, gems, item, version, shiny, amount, boughtFrom, status)
    local gemamount = game:GetService("Players").LocalPlayer.leaderstats["💎 Diamonds"].Value
    local name = game.Players.LocalPlayer.Name
    local snipeMessage = ""
    local url, color

    if status then
        snipeMessage = "Successfully sniped a "
        url = getgenv().webhook
        color = tonumber(0x00ff00)
        if string.find(item, "Huge") then
        tag = "<@870106984236609656> NEW HUGE BABY"
        elseif string.find(item, "Titanic") and item ~= "Titanic Christmas Present" then
            tag = "@everyone RAWRRR GOT TITANIC BRO"
        end
    else
        snipeMessage = "Failed to snipe a "
        url = getgenv().failedwebhook
        color = tonumber(0xff0000)
    end
    
    local tag = ""
    if version then
        if version == 2 then
            version = "**Rainbow** "
        elseif version == 1 then
            version = "**Golden** "
        end
    else
       version = ""
    end
    
    snipeMessage = snipeMessage .. version
    
    if shiny then
        snipeMessage = snipeMessage .. " **Shiny** "
    end
    
    snipeMessage = snipeMessage .. "**" .. (item) .. "**"
    
    if amount == nil then
        amount = 1
    end
    
    message1 = {
        ['content'] = tag,
        ['embeds'] = {
            {
                ['title'] = snipeMessage,
                ["color"] = color,
                ["timestamp"] = DateTime.now():ToIsoDate(),
                ['fields'] = {
                    {
                        ['name'] = "__Account Name:__",
                        ['value'] = "||" .. tostring(name) .. "||",
                    },
                    {
                        ['name'] = "__Price:__",
                        ['value'] = tostring(gems) .. " 💎",
                    },
                    {
                        ['name'] = "__Purchased From:__",
                        ['value'] = "||" .. tostring(boughtFrom) .. "||",
                    },
                    {
                        ['name'] = "__Amount:__",
                        ['value'] = tostring(amount) .. "x",
                    },
                    {
                        ['name'] = "__Remaining Gems:__",
                        ['value'] = tostring(gemamount) .. " 💎",
                    },      
                    {
                        ['name'] = "__Pet ID:__",
                        ['value'] = "||" .. tostring(uid) .. "||",
                    },
                },
            },
        }
    }

    task.spawn(function()
        local http = game:GetService("HttpService")
        local jsonMessage = http:JSONEncode(message1)
        http:PostAsync(url, jsonMessage)
    end)
end

local function checklisting(uid, gems, item, version, shiny, amount, username, playerid)
    local Library = require(game.ReplicatedStorage:WaitForChild('Library'))
    gems = tonumber(gems)
    local type = {}
    local status
    pcall(function()
        type = Library.Directory.Pets[item]
end)

    if amount == nil then
        amount = 1
    end
    
    if type.exclusiveLevel and gems / amount <= 10000 and item ~= "Banana" and item ~= "Coin" then
        local boughtf = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        task.wait(3)
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        local bought1 = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true or bought1 == true or boughtf == true then
            local statusb = true
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        else if bought == false or bought1 == false or boughtf == false then
            local statusb = false
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        end
    elseif item == "Titanic Christmas Present" and gems / amount <= 25000 then
        local boughtf = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        task.wait(3)
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        local bought1 = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true or bought1 == true or boughtf == true then
            local statusb = true
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        else if bought == false or bought1 == false or boughtf == false then
            local statusb = false
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        end
    elseif string.find(item, "Exclusive") and gems / amount <= 25000 then
        local boughtf = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        task.wait(3)
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        local bought1 = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true or bought1 == true or boughtf == true then
            local statusb = true
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        else if bought == false or bought1 == false or boughtf == false then
            local statusb = false
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        end
    elseif type.huge and gems / amount <= 1000000 then
        local boughtf = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        task.wait(3)
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        local bought1 = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true or bought1 == true or boughtf == true then
            local statusb = true
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        else if bought == false or bought1 == false or boughtf == false then
            local statusb = false
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        end
    elseif type.titanic and gems / amount <= 10000000 then
        local boughtf = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        task.wait(3)
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        local bought1 = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true or bought1 == true or boughtf == true then
            local statusb = true
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        else if bought == false or bought1 == false or boughtf == false then
            local statusb = false
            processListingInfo(uid, gems, item, version, shiny, amount, username, statusb)
        end
    end
end

Booths_Broadcast.OnClientEvent:Connect(function(username, message)
    if type(message) == "table" and message['PlayerID'] ~= nil then
        local playerID = message['PlayerID']
        local listing = message["Listings"]
        for key, value in pairs(listing) do
            if type(value) == "table" then
                local uid = key
                local gems = value["DiamondCost"]
                local itemdata = value["ItemData"]

                if itemdata then
                    local data = itemdata["data"]

                    if data then
                        local item = data["id"]
                        local version = data["pt"]
                        local shiny = data["sh"]
                        local amount = data["_am"]
                        checklisting(uid, gems, item, version, shiny, amount, username , playerID)
                    end
                end
            end
        end
    end
end)

TeleportService.TeleportInitFailed:Connect(function(player, resultEnum, msg)
                print(string.format("server: teleport %s failed, resultEnum:%s, msg:%s", player.Name, tostring(resultEnum), msg))
                wait(5)
                jumpToServer()
        end) 


local function jumpToServer() 
    local sfUrl = "https://games.roblox.com/v1/games/%s/servers/Public?sortOrder=%s&limit=%s&excludeFullGames=true" 
    local req = request({ Url = string.format(sfUrl, 15502339080, "Desc", 100) }) 
    local body = game:GetService("HttpService"):JSONDecode(req.Body) 
    local deep = math.random(1, 3)
    if deep > 1 then 
        for i = 1, deep, 1 do 
            req = request({ Url = string.format(sfUrl .. "&cursor=" .. body.nextPageCursor, 15502339080, "Desc", 100) }) 
            body = game:GetService("HttpService"):JSONDecode(req.Body) 
            task.wait(0.1)
        end 
    end 
    local servers = {} 
    if body and body.data then 
        for i, v in next, body.data do 
            if type(v) == "table" and tonumber(v.playing) and tonumber(v.maxPlayers) and v.playing < v.maxPlayers and v.id ~= game.JobId then
                table.insert(servers, 1, v.id)
            end
        end
    end
    local randomCount = #servers
    local nextrandom = math.random(1, randomCount)
    if not randomCount then
        randomCount = 2
    end
    game:GetService("TeleportService"):TeleportToPlaceInstance(15502339080, servers[math.random(1, nextrandom)], game:GetService("Players").LocalPlayer) 
end

while wait(5) do
    local MaxPing = 500
    PlayerInServer = #Players:GetPlayers()
    if PlayerInServer < 35 or os.time() >= ostimeold + 1000 then
        jumpToServer()
        break
    end
    if game.Players.LocalPlayer:GetNetworkPing() * 2000 > MaxPing then
        jumpToServer()
    end
    for count = 1, #alts, 1 do
        if game.Players:FindFirstChild(alts[count]) and alts[count] ~= game:GetService("Players").LocalPlayer.Name then
            jumpToServer()
            break
        end
    end
end
