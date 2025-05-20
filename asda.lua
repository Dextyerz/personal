local Player = game.Players.LocalPlayer    
local Http = game:GetService("HttpService")
local TPS = game:GetService("TeleportService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local eventShopData = require(ReplicatedStorage.Data.EventShopData)

local Api = "https://games.roblox.com/v1/games/"
local _place, _id = game.PlaceId, game.JobId
local _servers = Api .. _place .. "/servers/Public?sortOrder=Desc&limit=100"

-- Set untuk menyimpan server yang sudah dicoba
local triedServers = {}
triedServers[_id] = true -- Tambahkan server saat ini agar tidak balik ke sini

-- Fungsi ambil list server
function ListServers(cursor)
	local raw = game:HttpGet(_servers .. ((cursor and "&cursor=" .. cursor) or ""))
	return Http:JSONDecode(raw)
end

-- Fungsi utama
task.spawn(function()
	while true do
		local stockChance = eventShopData["Candy Blossom"] and eventShopData["Candy Blossom"].StockChance or 0

		if stockChance > 0 then
			warn("✅ StockChance ditemukan:", stockChance)
			break
		end
        queue_on_teleport([[loadstring(game:HttpGetAsync("https://raw.githubusercontent.com/Dextyerz/personal/refs/heads/main/asda.lua"))()]])
		local Next
		repeat
			local Servers = ListServers(Next)
			for i, v in next, Servers.data do
				if v.playing < v.maxPlayers and not triedServers[v.id] then
					triedServers[v.id] = true -- tandai server ini agar tidak dicoba lagi

					warn("Teleporting to server:", v.id)
					local success, err = pcall(TPS.TeleportToPlaceInstance, TPS, _place, v.id, Player)
					if success then
						return -- Biarkan teleport berjalan
					else
						warn("Teleport gagal:", err)
					end
				end
			end
			Next = Servers.nextPageCursor
			task.wait(1)
		until not Next

		warn("🔁 Semua server dicoba, mengulang dalam 5 detik...")
		task.wait(5)
	end
end)
