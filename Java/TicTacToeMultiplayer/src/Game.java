import java.rmi.Remote;
import java.rmi.RemoteException;




public interface Game extends Remote{
	public void init() throws RemoteException;
	public boolean waitForPlayer() throws RemoteException;
	public void toggleMutex() throws RemoteException;
	public boolean makeTurn(int i) throws RemoteException;
	public char[] getMap() throws RemoteException;
	public int checkEnd() throws RemoteException;

}
