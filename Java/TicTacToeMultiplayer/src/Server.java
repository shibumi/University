import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;



public class Server {
  /**
   * RMI-Server Starten mit inbuild Multithreading..
   */
	public static void main(String[] args) throws RemoteException {
		String gamename = "tictactoe";
		int port = (args.length > 0) ? Integer.parseInt(args[0]) : 8023;
		Registry registry = LocateRegistry.createRegistry(port);
		GameImpl game = new GameImpl();
		try {
			registry.rebind(gamename, game);
		} catch (Exception e) {
			System.out.println("");
		}
		System.out.println("Binding registry to Port: " + port +" was successful");
		System.out.println("Server was started...");

	}

}
