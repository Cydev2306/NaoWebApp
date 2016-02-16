<?php
class Sound extends Zend_Db_Table_Abstract
{
	protected $_name='sound';
	protected $_primary=array('id');
	
	public function selectVolume()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = $this->select()->from($this);
		return $db->query($requete)->fetchAll();
	}
	
	public function updateSound($value)
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'UPDATE sound SET volume ='.$value;
		return $db->query($requete)->fetch();
	}
}