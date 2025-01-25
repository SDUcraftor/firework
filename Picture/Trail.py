"""
        private void explodeBall(double size, int amount, IntList colors, IntList targetColors, boolean trail, boolean flicker) {
            double d = this.x;
            double e = this.y;
            double f = this.z;

            for(int i = -amount; i <= amount; ++i) {
                for(int j = -amount; j <= amount; ++j) {
                    for(int k = -amount; k <= amount; ++k) {
                        double g = (double)j + (this.random.nextDouble() - this.random.nextDouble()) * 0.5;
                        double h = (double)i + (this.random.nextDouble() - this.random.nextDouble()) * 0.5;
                        double l = (double)k + (this.random.nextDouble() - this.random.nextDouble()) * 0.5;
                        double m = Math.sqrt(g * g + h * h + l * l) / size + this.random.nextGaussian() * 0.05;
                        this.addExplosionParticle(d, e, f, g / m, h / m, l / m, colors, targetColors, trail, flicker);
                        if (i != -amount && i != amount && j != -amount && j != amount) {
                            k += amount * 2 - 1;
                        }
                    }
                }
            }
        }

                private void addExplosionParticle(double x, double y, double z, double velocityX, double velocityY, double velocityZ, IntList colors, IntList targetColors, boolean trail, boolean flicker) {
            Explosion explosion = (Explosion)this.particleManager.addParticle(ParticleTypes.FIREWORK, x, y, z, velocityX, velocityY, velocityZ);
            explosion.setTrail(trail);
            explosion.setFlicker(flicker);
            explosion.setAlpha(0.99F);
            explosion.setColor((Integer)Util.getRandom(colors, this.random));
            if (!targetColors.isEmpty()) {
                explosion.setTargetColor((Integer)Util.getRandom(targetColors, this.random));
            }
        }
"""
