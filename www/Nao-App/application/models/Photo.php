<?php
class Photo extends Zend_Db_Table_Abstract
{
	protected $_name='photo';
	protected $_primary=array('idPhoto');
	
	public function selectAll()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = $this->select()->from($this);
		return $db->query($requete)->fetchAll();
	}
	
	public function selectOne($id)
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = $this->select()->from($this)->where('idPhoto='.$id);
		return $db->query($requete)->fetch();
	}
	
	public function getIdMax()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'SELECT MAX(idPhoto) FROM photo';
		return $db->query($requete)->fetch();
	}
	
	public function getPremiere()
	{//retourne les 4 dernieres photos
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'SELECT * FROM photo ORDER BY idPhoto DESC LIMIT 0,4';
		return $db->query($requete)->fetchAll();
	}
	
	public function getQuatre($last)
	{//retourne la suite des photos en appel ajax
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'SELECT * FROM photo WHERE idPhoto < '.$last.' ORDER BY idPhoto DESC LIMIT 0,4';
		return $db->query($requete)->fetchAll();
	}
}