local osclock = os.clock()
local ostime = os.time()
local TeleportService = game:GetService("TeleportService")
repeat wait() until game:IsLoaded()

setfpscap(8)
game:GetService("RunService"):Set3dRenderingEnabled(false)
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

if not getgenv().a then
    getgenv().a = true
    local vu = game:GetService("VirtualUser")
    game:GetService("Players").LocalPlayer.Idled:connect(function()
        vu:Button2Down(Vector2.new(0,0),workspace.CurrentCamera.CFrame)
        wait(1)
        vu:Button2Up(Vector2.new(0,0),workspace.CurrentCamera.CFrame)
    end)
    
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


local function processListingInfo(uid, gems, item, version, shiny, amount, boughtFrom)
    local gemamount = game:GetService("Players").LocalPlayer.leaderstats["💎 Diamonds"].Value
    local name = game.Players.LocalPlayer.Name
    local snipeMessage = "Successfully sniped a "
    local tag = ""
    if version then
        if version == 2 then
            version = "Rainbow "
        elseif version == 1 then
            version = "Golden "
        end
    else
       version = ""
    end
    
    snipeMessage = snipeMessage .. version
    
    if shiny then
        snipeMessage = snipeMessage .. " Shiny "
    end
    
    snipeMessage = snipeMessage .. "**" .. (item) .. "**"
    
    if amount == nil then
        amount = 1
    end

    if string.find(item, "Huge") then
        tag = "<@870106984236609656> NEW HUGE BABY"
    elseif string.find(item, "Titanic") and item ~= "Titanic Christmas Present" then
        tag = "@everyone RAWRRR GOT TITANIC BRO"
    end
    
    message1 = {
        ['content'] = tag,
        ['embeds'] = {
            {
                ['title'] = snipeMessage,
                ["color"] = tonumber(0x33dd99),
                ["timestamp"] = DateTime.now():ToIsoDate(),
                ['fields'] = {
                    {
                        ['name'] = "Account Name:",
                        ['value'] = "||" .. tostring(name) .. "||",
                    },
                    {
                        ['name'] = "Price:",
                        ['value'] = tostring(gems) .. " 💎",
                    },
                    {
                        ['name'] = "Purchased From:",
                        ['value'] = "||" .. tostring(boughtFrom) .. "||",
                    },
                    {
                        ['name'] = "Amount:",
                        ['value'] = tostring(amount) .. "x",
                    },
                    {
                        ['name'] = "Remaining Gems:",
                        ['value'] = tostring(gemamount) .. " 💎",
                    },      
                    {
                        ['name'] = "Pet ID:",
                        ['value'] = "||" .. tostring(uid) .. "||",
                    },
                },
            },
        }
    }

    local http = game:GetService("HttpService")
    local jsonMessage = http:JSONEncode(message1)
    http:PostAsync(getgenv().webhook, jsonMessage)
end

local function checklisting(uid, gems, item, version, shiny, amount, username, playerid)
    local Library = require(game.ReplicatedStorage:WaitForChild('Library'))
    gems = tonumber(gems)
    local type = {}
    pcall(function()
        type = Library.Directory.Pets[item]
end)

    if amount == nil then
        amount = 1
    end
    
    if type.exclusiveLevel and gems / amount <= 10000 and item ~= "Banana" and item ~= "Coin" then
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true then
            processListingInfo(uid, gems, item, version, shiny, amount, username)
        end
    elseif item == "Titanic Christmas Present" and gems / amount <= 25000 then
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true then
            processListingInfo(uid, gems, item, version, shiny, amount, username)
        end
    elseif string.find(item, "Exclusive") and gems / amount <= 25000 then
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true then
            processListingInfo(uid, gems, item, version, shiny, amount, username)
        end
    elseif type.huge and gems / amount <= 1000000 then
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true then
            processListingInfo(uid, gems, item, version, shiny, amount, username)
        end     
    elseif type.titanic and gems / amount <= 10000000 then
        local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
        if bought == true then
            processListingInfo(uid, gems, item, version, shiny, amount, username)
        end
    end
end

local function printTable(tab, indent)
    indent = indent or 0
    for key, value in pairs(tab) do
        if type(value) == "table" then
            print(("\t"):rep(indent) .. key .. " (table):")
            printTable(value, indent + 1)
        else
            print(("\t"):rep(indent) .. key .. ":", value)
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
    local deep = math.random(1, 4)
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


Players.PlayerRemoving:Connect(function(player)
    PlayerInServer = #Players:GetPlayers()
    if PlayerInServer < 25 then
        jumpToServer()
    end
end) 

while wait(0.1) do
    if os.time() >= ostime + 1000 then
        jumpToServer()
        break
    end
    for count = 1, #alts, 1 do
        if game.Players:FindFirstChild(alts[count]) and alts[count] ~= game:GetService("Players").LocalPlayer.Name then
            jumpToServer()
            break
        end
    end
end
