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

Players.PlayerRemoving:Connect(function(plr)
    if plr == game.Players.LocalPlayer then
      game:GetService('TeleportService'):Teleport(game.PlaceId)
    end
end)

local bb = game:GetService("VirtualUser")
game:GetService("Players").LocalPlayer.Idled:Connect(function()
    bb:CaptureController()
    bb:ClickButton2(Vector2.new())
end)

local function GetThumbnailImage(ThumbnailID)
    local Image = string.split(ThumbnailID, "rbxassetid://")[2]
    Image = game:HttpGet("https://thumbnails.roproxy.com/v1/assets?assetIds=" .. Image .. "&returnPolicy=PlaceHolder&size=420x420&format=Png&isCircular=false")
    Image = game:GetService("HttpService"):JSONDecode(Image).data[1].imageUrl
    return Image
end

local function processListingInfo(uid, gems, item, version, shiny, amount, boughtFrom, thumb, goldenthum)
    local gemamount = game:GetService("Players").LocalPlayer.leaderstats["💎 Diamonds"].Value
    local name = game.Players.LocalPlayer.Name
    local snipeMessage = "Successfully sniped a "
    local tag = ""
    local thumburl = "https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg"
    if version then
        if version == 2 then
            version = "Rainbow "
            thumburl = GetThumbnailImage(thumb)
        elseif version == 1 then
            version = "Golden "
            thumburl = GetThumbnailImage(goldenthum)
        end
    else
        version = ""
        thumburl = GetThumbnailImage(thumb)
    end
    
    snipeMessage = snipeMessage .. version
    
    if shiny then
        snipeMessage = snipeMessage .. "Shiny "
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
                ['thumbnail'] = {
                    ['url'] = thumburl,
                },
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
    local success, response = pcall(function()
            http:PostAsync(getgenv().webhook, jsonMessage)
    end)
    if success == false then
            local response = request({
            Url = webhook,
            Method = "POST",
            Headers = {
                ["Content-Type"] = "application/json"
            },
            Body = jsonMessage
        })
    end
end



local function checklisting(uid, gems, item, version, shiny, amount, username, playerid)
    local Library = require(game.ReplicatedStorage:WaitForChild('Library'))
    gems = tonumber(gems)
    local type = {}
    pcall(function()
        type = Library.Directory.Pets[item]
    end)

    if type.exclusiveLevel and gems / amount <= 10000 and item ~= "Banana" and item ~= "Coin" then
        spawn(function()
            local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
            if bought == true then
                local Thumbnail = type.thumbnail
                local GoldenThumbnail = type.goldenThumbnail
                processListingInfo(uid, gems, item, version, shiny, amount, username, Thumbnail, GoldenThumbnail)
            end
        end)
    elseif item == "Titanic Christmas Present" and gems / amount <= 25000 then
        spawn(function()
            local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
            if bought == true then
                processListingInfo(uid, gems, item, version, shiny, amount, username)
            end
        end)
    elseif string.find(item, "Exclusive") and gems / amount <= 25000 then
        spawn(function()
            local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
            if bought == true then
                processListingInfo(uid, gems, item, version, shiny, amount, username)
            end
        end)
    elseif type.huge and gems / amount <= 1000000 then
        spawn(function()
            local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
            if bought == true then
                local Thumbnail = type.thumbnail
                local GoldenThumbnail = type.goldenThumbnail
                processListingInfo(uid, gems, item, version, shiny, amount, username, Thumbnail, GoldenThumbnail)
            end
        end)
    elseif type.titanic and gems / amount <= 10000000 then
        spawn(function()
            local bought = game:GetService("ReplicatedStorage").Network.Booths_RequestPurchase:InvokeServer(playerid, uid)
            if bought == true then
                local Thumbnail = type.thumbnail
                local GoldenThumbnail = type.goldenThumbnail
                processListingInfo(uid, gems, item, version, shiny, amount, username, Thumbnail, GoldenThumbnail)
            end
        end)
    end
end

Booths_Broadcast.OnClientEvent:Connect(function(username, message)
    local playerIDSuccess, playerError = pcall(function()
	playerID = message['PlayerID']
    end)
    if playerIDSuccess then
        if type(message) == "table" then
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
    end
end)

TeleportService.TeleportInitFailed:Connect(function(player, resultEnum, msg)
                print(string.format("server: teleport %s failed, resultEnum:%s, msg:%s", player.Name, tostring(resultEnum), msg))
                wait(10)
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
    if not randomCount then
        randomCount = 2
    end
    game:GetService("TeleportService"):TeleportToPlaceInstance(15502339080, servers[math.random(1, randomCount)], game:GetService("Players").LocalPlayer) 
end

while wait(0.1) do
    PlayerInServer = #Players:GetPlayers()
    if PlayerInServer < 25 or os.time() >= ostime + 1080 then
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
