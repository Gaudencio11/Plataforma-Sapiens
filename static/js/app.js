// Scene & Controls
const container = document.body
const scene = new THREE.Scene()
const camera = new THREE.PerspectiveCamera(90, window.innerWidth / window.innerHeight, 0.1, 200 )
const renderer = new THREE.WebGLRenderer({antialias: true})                              //tem q declarar o renderer antes do proximo
const controls = new THREE.OrbitControls(camera, renderer.domElement)  //deve ter o THREE.
const tooltip = document.querySelector('.tooltip')  
let tooltipActive = false

renderer.setSize(window.innerWidth, window.innerHeight)
container.appendChild(renderer.domElement)

controls.enablePan = false
controls.enableZoom = true
controls.autoRotate = false
controls.autoRotateSpeed = 0.2
controls.enableDamping = true


camera.position.set(-1, 0, 0.1)
controls.update()

// Sphere (Object)
const geometry = new THREE.SphereGeometry(50, 32, 32)
const texture = new THREE.TextureLoader().load('../static/images/audit.jpg')
texture.wrapS = THREE.RepeatWrapping    // Inverts texture in the X axis of the sphere (inverte a foto)
texture.repeat.x = - 1

const material = new THREE.MeshBasicMaterial({
    map: texture,
    side: THREE.DoubleSide
})
//material.transparent = true -> sem isso não fica fundo preto na coruja

// Mesh
const sphere = new THREE.Mesh(geometry, material)
scene.add(sphere)   // assim ao invés de this.sphere aparece a imagem de fundo

// Renderer 
// Essa função é responsável por renderizar a cena na tela

function animate() {
	requestAnimationFrame(animate)
    controls.update()
	renderer.render(scene, camera)
}
animate()


// Allowing canvas responsiveness maintaining ratio
function onResize() {
    renderer.setSize(window.innerWidth, window.innerHeight)
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    
}

// Raycasting is used for mouse picking (working out what objects in the 3d space the mouse is over)
const rayCaster = new THREE.Raycaster()
function onClick(e){
    // Nós convertemos a posição do mouse no quadro da câmera
    let mouse = new THREE.Vector2(
        (e.clientX / window.innerWidth) * 2 - 1,
        - (e.clientY / window.innerHeight) * 2 + 1
    )
    console.log(mouse)
    rayCaster.setFromCamera(mouse, camera)
    const intersects = rayCaster.intersectObjects(texture) //tava texture
    if(intersects.length < 0) {
        console.log(intersects[0].point)
    }
}
container.addEventListener('click', onClick)
    /*let intersects = rayCaster.intersectObject(sphere)
    if (intersects.length > 0) {
        addTooltip1(intersects[0].point) // Allows placing manually the positions
        
    */

function abreLink(){
    if (addTooltip1) {
        window.open(rooms_names[0]['url']);
    }
    if (addTooltip2) {
        window.open('http://www.americanas.com.br');
    }
}
/*     if (addTooltip3) {
        window.open('http://www.americanas.com.br');
    }
    if (addTooltip4) {
        window.open('http://www.unipe.com.br');
    }
    if (addTooltip5) {
        window.open('http://www.unicid.com.br');
    }
    if (addTooltip6) {
        window.open('http://www.submarino.com.br');
    }
} */

// Tooltip (sprite) Hotspot!
//1
function addTooltip1 (position, name) {
    let spriteMap = new THREE.TextureLoader().load('../static/images/largeinfotie.png')
    let spriteMaterial = new THREE.SpriteMaterial({ 
        map: spriteMap 
    })
    let sprite = new THREE.Sprite(spriteMaterial)
    sprite.name = name
    sprite.position.copy(position.clone().normalize().multiplyScalar(30))
    sprite.scale.multiplyScalar(4)
    //let position = new THREE.Vector3(20, 0.3, -5.2)
    scene.add(sprite)
}

//2
function addTooltip2 (position, name) {
    let spriteMap = new THREE.TextureLoader().load('../static/images/largeinfotie.png')
    let spriteMaterial = new THREE.SpriteMaterial({ 
        map: spriteMap 
    })
    let sprite = new THREE.Sprite(spriteMaterial)
    sprite.name = name
    sprite.position.copy(position.clone().normalize().multiplyScalar(30))
    sprite.scale.multiplyScalar(3)
    //let position = new THREE.Vector3(20, 0.3, -5.2)
    scene.add(sprite)
}
    
//3
function addTooltip3 (position, name) {
    let spriteMap = new THREE.TextureLoader().load('../static/images/largeinfotie.png')
    let spriteMaterial = new THREE.SpriteMaterial({ 
        map: spriteMap 
    })
    let sprite = new THREE.Sprite(spriteMaterial)
    sprite.name = name
    sprite.position.copy(position.clone().normalize().multiplyScalar(30))
    sprite.scale.multiplyScalar(2)
    //let position = new THREE.Vector3(20, 0.3, -5.2)
    scene.add(sprite)
}

//4
function addTooltip4 (position, name) {
    let spriteMap = new THREE.TextureLoader().load('../static/images/largeinfotie.png')
    let spriteMaterial = new THREE.SpriteMaterial({ 
        map: spriteMap 
    })
    let sprite = new THREE.Sprite(spriteMaterial)
    sprite.name = name
    sprite.position.copy(position.clone().normalize().multiplyScalar(30))
    sprite.scale.multiplyScalar(3)
    //let position = new THREE.Vector3(20, 0.3, -5.2)
    scene.add(sprite)
}

//5
function addTooltip5 (position, name) {
    let spriteMap = new THREE.TextureLoader().load('../static/images/largeinfotie.png')
    let spriteMaterial = new THREE.SpriteMaterial({ 
        map: spriteMap 
    })
    let sprite = new THREE.Sprite(spriteMaterial)
    sprite.name = name
    sprite.position.copy(position.clone().normalize().multiplyScalar(30))
    sprite.scale.multiplyScalar(3)
    //let position = new THREE.Vector3(20, 0.3, -5.2)
    scene.add(sprite)
}

//6
function addTooltip6 (position, name) {
    let spriteMap = new THREE.TextureLoader().load('../static/images/largeinfotie.png')
    let spriteMaterial = new THREE.SpriteMaterial({ 
        map: spriteMap 
    })
    let sprite = new THREE.Sprite(spriteMaterial)
    sprite.name = name
    sprite.position.copy(position.clone().normalize().multiplyScalar(30))
    sprite.scale.multiplyScalar(3)
    //let position = new THREE.Vector3(20, 0.3, -5.2)
    scene.add(sprite)
}

function onMouseMove(e){
    let mouse = new THREE.Vector2(
        (e.clientX / window.innerWidth) * 2 - 1,
        -(e.clientY / window.innerHeight) * 2 + 1
    )
    rayCaster.setFromCamera(mouse, camera)
    let foundSprite = false
    let intersects = rayCaster.intersectObjects(scene.children)
    intersects.forEach(function (intersect){
        if(intersect.object.type === 'Sprite') {
            //console.log(intersect.object.name)
            let p = intersect.object.position.clone().project(camera)
            tooltip.style.top = ((-1 * p.y + 1) * window.innerHeight / 2) + 'px'
            tooltip.style.left = ((p.x + 1) * window.innerWidth / 2) + 'px'
            tooltip.classList.add('is-active')
            tooltip.innerHTML = intersect.object.name
            tooltipActive = true
            foundSprite = true
            console.log(intersect.object.scale)
            console.log(tooltip.style.top)
        }
    })    
    if (foundSprite === false && tooltipActive) {
        tooltip.classList.remove('is-active')
    }
}



// Inserindo as corujas na foto
addTooltip1(new THREE.Vector3(50, -3, -25), rooms_names[0]['nome'])
addTooltip2(new THREE.Vector3(50, -5, -150), rooms_names[1]['nome'])
addTooltip3(new THREE.Vector3(50, -5, -1900), rooms_names[2]['nome'])
addTooltip4(new THREE.Vector3(50, -5, 18), 'Jogos Teens')
addTooltip5(new THREE.Vector3(50, -5, 80), 'Espaço Kids')
addTooltip6(new THREE.Vector3(50, -5, 300), 'Contato')

function onMouseWheel(event) {
    if (event.wheelDeltaY) { // WebKit
      camera.fov -= event.wheelDeltaY * 0.05;
    } else if (event.wheelDelta) { // Opera / IE9
      camera.fov -= event.wheelDelta * 0.05;
    } else if (event.detail) { // Firefox
      camera.fov += event.detail * 1.0;
    }
    camera.fov = Math.max(40, Math.min(100, camera.fov))
    camera.updateProjectionMatrix()
}

document.addEventListener('mousewheel', onMouseWheel, false)
document.addEventListener('DOMMouseScroll', onMouseWheel, false)
// Adding click event to the container (constant that represents any document.body element)
window.addEventListener('resize', onResize)
container.addEventListener('mousemove', onMouseMove)
tooltip.addEventListener('click', abreLink)

print(parametro)