using System.Collections.Generic;
using UnityEngine;

public class GroundManager : MonoBehaviour
{
    public GameObject groundPrefab; // The ground tile prefab
    public Transform playerTransform; // The player's transform

    private float spawnX = -5.0f; // Starting position of the first tile in X direction
    private float spawnZ = -5.0f; // Starting position of the first tile in Z direction
    private float tileLength = 10.0f; // Length of a single tile
    private int tilesOnScreen = 6; // Number of tiles on screen at a time

    private List<GameObject> activeTiles;
    
    void Start()
    {
        activeTiles = new List<GameObject>();
        
        for (int i = 0; i < tilesOnScreen; i++)
        {
            SpawnTile();
        }
    }

   void Update()
   {
       if (playerTransform.position.x - spawnX > (tilesOnScreen - 1) * tileLength || 
           playerTransform.position.z - spawnZ > (tilesOnScreen - 1) * tileLength)
       {
           SpawnTile();
           DeleteTile();
       }
   }

   void SpawnTile()
   {
       GameObject go;
       go = Instantiate(groundPrefab) as GameObject;
       go.transform.SetParent(transform);
       go.transform.position = new Vector3(spawnX, 0, spawnZ);
       
       if(Random.value < 0.5)
            spawnX += tileLength;
        else 
            spawnZ += tileLength;

       activeTiles.Add(go);
   }

   void DeleteTile()
   {
      Destroy(activeTiles[0]);
      activeTiles.RemoveAt(0);
      
      if(Random.value < 0.5)
            spawnX -= tileLength;
        else 
            spawnZ -= tileLength;
   }
}
