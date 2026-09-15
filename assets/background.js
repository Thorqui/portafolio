try {
            const { Scene, PerspectiveCamera, WebGLRenderer, BufferGeometry, Float32BufferAttribute, PointsMaterial, Points, LineSegments, LineBasicMaterial, Vector3, Vector2, Clock, AdditiveBlending, CanvasTexture } = await import('three');
            const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

            // Función para crear textura redonda difuminada
            function createCircleTexture() {
                const canvas = document.createElement('canvas');
                canvas.width = 32;
                canvas.height = 32;
                const context = canvas.getContext('2d');
                const gradient = context.createRadialGradient(16, 16, 0, 16, 16, 16);
                gradient.addColorStop(0, 'rgba(255,255,255,1)');
                gradient.addColorStop(0.2, 'rgba(210,230,255,0.8)');
                gradient.addColorStop(0.5, 'rgba(100,150,255,0.2)');
                gradient.addColorStop(1, 'rgba(0,0,0,0)');
                context.fillStyle = gradient;
                context.fillRect(0,0,32,32);
                return new CanvasTexture(canvas);
            }
            const circleTexture = createCircleTexture();

            const canvas = document.getElementById('bg-canvas');
            const scene = new Scene();
            // Ligero tinte de color para el fondo espacial
            scene.background = null;

            const camera = new PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 5;
            const renderer = new WebGLRenderer({ canvas, antialias: window.innerWidth > 768, alpha: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
            const particleCount = window.innerWidth <= 768 ? 1200 : 3000;
            const positions = new Float32Array(particleCount * 3);
            const colors = new Float32Array(particleCount * 3);

            for(let i = 0; i < positions.length; i++) {
                positions[i] = (Math.random() - 0.5) * 150;
            }
            // Dar un tono ligeramente azulado aleatorio a las estrellas
            for(let i = 0; i < particleCount; i++) {
                colors[i*3] = 0.6 + Math.random() * 0.4;     // R
                colors[i*3+1] = 0.8 + Math.random() * 0.2;   // G
                colors[i*3+2] = 1.0;                         // B
            }

            const particlesGeometry = new BufferGeometry();
            particlesGeometry.setAttribute('position', new Float32BufferAttribute(positions, 3));
            particlesGeometry.setAttribute('color', new Float32BufferAttribute(colors, 3));

            const particlesMaterial = new PointsMaterial({
                size: 0.25,
                sizeAttenuation: true,
                transparent: true,
                opacity: 0.8,
                map: circleTexture,
                blending: AdditiveBlending,
                depthWrite: false,
                vertexColors: true
            });
            const backgroundParticles = new Points(particlesGeometry, particlesMaterial);
            scene.add(backgroundParticles);


            const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
            let frame = 0;
            let last = 0;
            function render(now = 0) {
                frame = 0;
                if (document.hidden) return;
                if (now - last > 33 || motion.matches) {
                    if (!motion.matches) {
                        backgroundParticles.rotation.y = now * 0.000015;
                        backgroundParticles.rotation.x = now * 0.000006;
                    }
                    renderer.render(scene, camera);
                    last = now;
                }
                if (!motion.matches) frame = requestAnimationFrame(render);
            }
            function restart() {
                cancelAnimationFrame(frame);
                render();
            }
            motion.addEventListener('change', restart);
            document.addEventListener('visibilitychange', restart);
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
                restart();
            });
            restart();
        } catch (error) {
            console.warn('Background unavailable; portfolio content remains accessible.', error);
        }
