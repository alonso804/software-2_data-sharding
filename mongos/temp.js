sh.addShard("shard1rs/shard1s1:27017,shard1s2:27017,shard1s3:27017")

sh.enableSharding("is2-shard")

sh.shardCollection("is2-shard.test", { name: "hashed" } )
