<?php
class User extends Zend_Db_Table_Abstract
{
	protected $_name='user';
	
	//clef primaire
	protected $_primary=array('idUser');
	
	//fonction qui récupère tous les projets
	public function selectAll()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = $this->select()->from($this);
		return $db->query($requete)->fetchAll();
	}
	public function selectOne($idUser)
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = $this->select()->from($this)->where('idUser='.$idUser);
		return $db->query($requete)->fetch();
	}
	public function getIdMax()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'SELECT MAX(idUser) FROM user';
		return $db->query($requete)->fetch();
	}
	public function updateDateConnexion($date)
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'UPDATE user SET dateConnexion =\''.$date.'\'';
		return $db->query($requete)->fetch();
	}
}