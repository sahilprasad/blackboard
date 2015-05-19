# Tic Tac Toe 
# by Sahil Prasad 

# ----------------
def move_rule
	puts "Enter a move (x, y) with the given scheme:"
	puts "3"
	puts "2"
	puts "1"
	puts " 1 2 3"
end

puts "Welcome to Tic-Tac-Toe!"
puts "Specify a name for Player One (will default to Charizard): "
$player_one = gets.chomp
if $player_one == "" 
	$player_one = "Charizard"
end
puts "Specify a name for Player Two (will default to Blastoise): "
$player_two = gets.chomp
if $player_two == ""
	$player_two = "Blastoise"
end 

puts "#{$player_one} vs. #{$player_two}!"
puts
move_rule
puts


$row1 = "     "
$row2 = "     "
$row3 = "     "

# functions 

def insert_dividers(row)
	row.insert(1, '|')
	row.insert(3, '|')
end 

insert_dividers($row1)
insert_dividers($row2)
insert_dividers($row3)

def print_board
	puts
	puts $row1
	puts $row2
	puts $row3 
	puts
end 

# make_move(int x, int y, string player)
# changes specified element of specified 
# row to reflect a move made by a player
def make_move(x, y, player)

	p = tokenize(player)
	case y
	when 1
		row = $row3
	when 2
		row = $row2
	when 3
		row = $row1
	end 

	target = row[x-1] if x == 1
	target = row[x] if x == 2
	target = row[x+1] if x == 3

	if target != " "
		raise NoMethodError
	else 
		puts "#{$current_player} moved to (#{x},#{y})!"
		row[x-1] = p if x == 1
		row[x] = p if x == 2
		row[x+1] = p if x == 3
		print_board
	end 
end 

# deletes anything in the input that is not a digit 
# checks to see if the remaining string corresponds to
# valid input, and otherwise raises a RuntimeError 
# if the input corresponds to a valid move, make_move 
# is called with the integer versions of x and y 
def get_move(move) 
	move = move.delete('^0-9')
	if move.length > 2 || move.length == 0
		raise "Invalid move."
	else 
		x = move[0]
		y = move[1]
		make_move(x.to_i, y.to_i, $current_player)
	end 
end 

def switch_player
	if $current_player == $player_one
		$current_player = $player_two
	else 
		$current_player = $player_one
	end 
end 

def other_player
	if $current_player == $player_one
		return $player_two
	else 
		return $player_one
	end 
end 

# constructs all of the horizontal, vertical, and diagonal 
# rows within the board, and checks to see if any of them 
# contains the token representation of the current player 
# three times. If so, it returns true because that player 
# has a winning row, otherwise, false. 
def check_win
	p = tokenize($current_player)
	vert1 = $row1[0] + $row2[0] + $row3[0]
	vert2 = $row1[2] + $row2[2] + $row3[2]
	vert3 = $row1[4] + $row2[4] + $row3[4]

	horz1 = vert1[0] + vert2[0] + vert3[0]
	horz2 = vert1[1] + vert2[1] + vert3[1]
	horz3 = vert1[2] + vert2[2] + vert3[2]

	diag1 = $row1[0] + $row2[2] + $row3[4]
	diag2 = $row3[0] + $row2[2] + $row1[4]

	winning_options = [vert1, vert2, vert3, horz1, horz2, horz3, diag1, diag2]
	if winning_options.any? {|x| (x.count p) >= 3}
		return true
	end 
end 



def tokenize(player)
	return player[0]
end 

def who_won
	puts "#{$current_player} has demolished #{other_player}"
end 

def exec_turn 
	puts "#{$current_player}'s turn!"
	move = gets.chomp 
	ask_again = true 
	while ask_again do 
		begin 
			get_move move 
			ask_again = false
		rescue NoMethodError, RuntimeError => boom 
			puts "Invalid move. Valid moves are of the form (x, y)."
			puts "Try again: "
			move = gets.chomp
		end 
	end 
end 


# main logic 

$current_player = [$player_one, $player_two].sample
$game_going = true
while $game_going do 
	exec_turn
	if check_win
		who_won 
		break
	else
		switch_player
	end
end 




