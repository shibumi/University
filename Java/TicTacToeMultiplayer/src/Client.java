import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.util.Scanner;




public class Client {
	/**
	 * Client - main-class 
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println("tictactoe - X first player - O second player");
		System.out.println("Choose a cell with typing the number in the cell");
		final int TURNS = 9;
		String gamename = "tictactoe";
		String targetHost = (args.length > 0 ) ? args[0] : "127.0.0.1";
		int targetPort = (args.length > 1 ) ? Integer.parseInt(args[1]) : 8023;
		try {
			Game game = (Game) Naming.lookup("rmi://" + targetHost + ":" + targetPort + "/" + gamename);
			game.init();
			while(game.waitForPlayer()){
				Thread.sleep(2000);
				System.out.println("Waiting for second player...");
			}
			System.out.println("Both players are connected.. let the games begin");
			Thread.sleep(2000);
			Scanner scan = new Scanner(System.in);
			int turn;
			int result;
			boolean end = false;
			boolean flag;
			for (int i = 0; i < TURNS; i++) {
				System.out.println("Waiting for turn of another player...");
				while(game.waitForPlayer()){
					Thread.sleep(1000);
					if(end) break;
					
				}
				showMap(game.getMap());
				result = game.checkEnd();
				if (result > 0){
					if((result) == 3){
						end = true;
						System.out.println("DRAW");
						break;
					}
					else if(result == 2){
						end = true;
						System.out.println("Second Player wins");
						break;
					}
					else if(result == 1){
						end = true;
						System.out.println("First Player wins");
						break;
					}
					
				}
				if(!game.waitForPlayer()){
					flag = true;
					game.toggleMutex();
					System.out.print("Please make your turn: ");
					while(flag){
						turn = scan.nextInt();
						if(turn < 0 || turn > 8){
							System.out.println("Wrong turn");
							System.out.print("New turn: ");
							continue;
						}
						if(!game.makeTurn(turn)){
							System.out.println("Wrong turn");
							System.out.print("New turn: ");
							continue;
						}
						else flag = false;
					}
					game.toggleMutex();
					Thread.sleep(1000);
					showMap(game.getMap());
					
					
					
				}
			}
			
		} catch (MalformedURLException | RemoteException | NotBoundException e) {
			System.out.println("Cannot contact the RMI Server");
		} catch (InterruptedException e) {
			System.out.println("something wrong with the sleeptimer..");
		}
		
		
	}
	
	public static void showMap(char[] map){
		int j = 0;
		for (int i = 0; i < map.length; i++) {
			System.out.print(map[i]);
			if(i == 0 || i == 1) System.out.print("|");
			if(i == 3 || i == 4) System.out.print("|");
			if(i == 6 || i == 7) System.out.print("|");
			j++;
			if(j == 3){
				System.out.println("");
				j = 0;
				if(i == 2 || i == 5) System.out.println("------");
			}
			
			
		}
	}


}
