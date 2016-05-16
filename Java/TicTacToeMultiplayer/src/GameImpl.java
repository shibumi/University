import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;


public class GameImpl extends UnicastRemoteObject implements Game{
	private enum Status {NONE,FIRST,SECOND};
	private Status mutex = Status.NONE;
	private char[] map = new char[9];
	private boolean token = true;

	public GameImpl() throws RemoteException {};
	
	public void init() throws RemoteException {
		if(mutex == Status.NONE) setMutex(Status.FIRST);
		else if(mutex == Status.FIRST){
			setMutex(Status.SECOND);
			for (int i = 0; i < map.length; i++) {
				map[i] = (char) ('0' + i);
			}
			
		}
	}
	
	public boolean waitForPlayer() throws RemoteException{
		if(getMutex() == Status.SECOND)return false; 
		else return true;
	}
	
	public void toggleMutex() throws RemoteException{
		if(getMutex() == Status.SECOND) setMutex(Status.FIRST);
		else if(getMutex() == Status.FIRST) setMutex(Status.SECOND);
	}
	
	public boolean makeTurn(int i) throws RemoteException{
		if(token){
			if(map[i] != 'X' && map[i] != 'O') {
				map[i] = 'X';
				toggleToken();
				return true;
			}
			else return false;
			
		}
		else {
			if(map[i] != 'X' && map[i] != 'O'){
				map[i] = 'O';
				toggleToken();
				return true;
			}
			else return false;
		}

	}
	
	public int checkEnd() throws RemoteException{
		Status status = checkWin();
		if(status == Status.FIRST) return 1;
		else if(status == Status.SECOND) return 2;
		int flag = 0;
		for (int i = 0; i < map.length; i++) {
			if(map[i] == 'X' || map[i] == 'O') flag++;
		}
		if (flag == 8){
			return 3;
		}
		return 0;
	}
	
	public Status checkWin(){
		if(map[0] == 'X' && map[1] == 'X' && map[2] == 'X') return Status.FIRST;
		if(map[0] == 'O' && map[1] == 'O' && map[2] == 'O') return Status.SECOND;
		if(map[3] == 'X' && map[4] == 'X' && map[5] == 'X') return Status.FIRST;
		if(map[3] == 'O' && map[4] == 'O' && map[5] == 'O') return Status.SECOND;
		if(map[6] == 'X' && map[7] == 'X' && map[8] == 'X') return Status.FIRST;
		if(map[6] == 'O' && map[7] == 'O' && map[8] == 'O') return Status.SECOND;
		if(map[0] == 'X' && map[3] == 'X' && map[6] == 'X') return Status.FIRST;
		if(map[0] == 'O' && map[3] == 'O' && map[6] == 'O') return Status.SECOND;
		if(map[1] == 'X' && map[4] == 'X' && map[7] == 'X') return Status.FIRST;
		if(map[1] == 'O' && map[4] == 'O' && map[7] == 'O') return Status.SECOND;
		if(map[2] == 'X' && map[5] == 'X' && map[8] == 'X') return Status.FIRST;
		if(map[2] == 'O' && map[5] == 'O' && map[8] == 'O') return Status.SECOND;
		if(map[0] == 'X' && map[4] == 'X' && map[8] == 'X') return Status.FIRST;
		if(map[0] == 'O' && map[4] == 'O' && map[8] == 'O') return Status.SECOND;
		if(map[2] == 'X' && map[4] == 'X' && map[6] == 'X') return Status.FIRST;
		if(map[2] == 'O' && map[4] == 'O' && map[6] == 'O') return Status.SECOND;
		return Status.NONE;
					
	}
	
	public void toggleToken(){
		if(token) token = false;
		else token = true;
	}

	public Status getMutex() {
		return mutex;
	}

	public void setMutex(Status mutex) {
		this.mutex = mutex;
	}
	
	public char[] getMap() throws RemoteException{
		return map;
	}
	
	
	

}
